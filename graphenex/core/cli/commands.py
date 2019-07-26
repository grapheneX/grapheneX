#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from graphenex.core.utils.helpers import check_os, get_modules, \
    mod_json_file, get_forbidden_namespaces, get_mod_json, get_presets
from graphenex.core.utils.logcl import GraphenexLogger
from graphenex.core.cli.help import Help

from terminaltables import AsciiTable
from PyInquirer import prompt, Validator, ValidationError
import textwrap
import secrets
import random
import json
import os
import re

logger = GraphenexLogger(__name__)

class ShellCommands(Help):
    def do_switch(self, arg):
        """Switch between modules or namespaces"""

        if not arg:
            logger.warn("'switch' command takes 1 argument.")
            return
        arg = arg.lower()
        if arg in self.modules.keys():
            logger.info(f"Switched to \"{arg}\" namespace." +
                        " Use 'list' command to see available modules.")
            self.namespace = arg
            self.module = ""
        else:
            self.do_use(arg)

    def complete_switch(self, text, line, begidx, endidx):
        """Complete switch command"""

        avb_namespaces = [i.lower() for i in self.modules.keys()]
        mline = line.lower().partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in avb_namespaces if s.startswith(mline)]

    def do_use(self, arg):
        """Use the hardening module"""

        if "/" in arg and arg.split("/")[0].lower() in self.modules.keys():
            self.namespace = arg.split("/")[0].lower()
            arg = arg.split("/")[1]

        def select_module_msg():
            logger.info(f"\"{self.module}\" module selected. Use 'harden' command " +
                        "for hardening or use 'info' for more information.")
        if not arg:
            logger.warn("'use' command takes 1 argument.")
            return
        module_found = False
        if self.namespace:
            for name, module in self.modules[self.namespace].items():
                if arg.lower() == name.lower():
                    module_found = True
                    self.module = name
                    select_module_msg()
        else:
            for k, v in self.modules.items():
                for name, module in v.items():
                    if arg.lower() == name.lower():
                        module_found = True
                        self.module = name
                        self.namespace = k
                        select_module_msg()
        if not module_found:
            logger.error(f"No module/namespace named \"{arg}\".")

    def complete_use(self, text, line, begidx, endidx):
        """Complete use command"""

        avb_modules = self.modules.get(self.namespace)
        if avb_modules is None:
            avb_modules = list()
            for key, value in self.modules.items():
                for name, module in value.items():
                    avb_modules.append(f"{key}/{name}")
        mline = line.lower().partition(' ')[2]
        # If namespace selected
        if '/' in mline:
            # title() -> given module string for getting rid of
            # the case sensitivity
            mline = mline.split('/')[0].lower() + "/" + \
                mline.split('/')[1].title()
        offs = len(mline) - len(text)
        # Get completed text with namespace
        comp_text = [s[offs:] for s in avb_modules if s.startswith(mline)]
        # If no namespace found
        if len(comp_text) == 0:
            # Try to complete with module names
            avb_modules = list()
            for key, value in self.modules.items():
                for name, module in value.items():
                    avb_modules.append(name)
            mline = mline.title()
            comp_text = [s[offs:] for s in avb_modules if s.startswith(mline)]
        return comp_text

    def do_info(self, arg):
        """Show information about the module"""

        if self.module:
            module = self.modules[self.namespace][self.module]
            print(f"\n\tNamespace: {self.namespace}\n\tModule: {module.name}\n\t" +
                f"Description: {module.desc}\n" + f"\tCommand: {module.command}\n")
        else:
            logger.error('No module selected.')

    def do_search(self, arg):
        """Search for modules"""

        search_table = [['Module', 'Description']]
        table = AsciiTable(search_table)
        max_width = table.column_max_width(1)

        if not arg:
            self.do_list(None)
            return
        if arg in self.modules.keys():
            for name, module in self.modules[arg].items():
                wrapped = '\n'.join(textwrap.wrap(module.desc, max_width - 40))
                table.table_data.append(
                    [arg + "/" + name, wrapped])
        else:
            for k, v in self.modules.items():
                for name, module in v.items():
                    if arg.lower() in name.lower():
                        wrapped = '\n'.join(textwrap.wrap(module.desc, max_width - 40))
                        table.table_data.append(
                            [k + "/" + name, wrapped])
        if len(table.table_data) > 1:
            print(table.table)
        else:
            logger.error(f"Nothing found for \"{arg}\".")

    def do_list(self, arg):
        """List available hardening modules"""

        modules_table = [['Module', 'Description']]
        table = AsciiTable(modules_table)
        max_width = table.column_max_width(1)

        if self.namespace:
            for name, module in self.modules[self.namespace].items(): 
                wrapped = '\n'.join(textwrap.wrap(module.desc, max_width - 40))
                table.table_data.append(
                    [self.namespace + "/" + name, wrapped])
        else:
            for k, v in self.modules.items():
                for name, module in v.items():
                    wrapped = '\n'.join(textwrap.wrap(module.desc, max_width - 40))
                    table.table_data.append(
                        [k + "/" + name, wrapped])
          
        print(table.table)

    def do_back(self, arg):
        """Go back from namespace or module"""

        if self.module:
            self.module = ""
        else:
            self.namespace = ""

    def do_manage(self, arg):
        """Add, edit or delete module"""

        def save_mod_json(data):
            with open(mod_json_file, 'w') as f:
                json.dump(data, f, indent=4)

        # Read modules.json
        data = get_mod_json()
        try:
            edit_prompt = [
                {
                    'type': 'list',
                    'name': 'option',
                    'message': 'What do you want to do?',
                    'choices': ["Add module", "Edit module", "Remove module"],
                }
            ]
            choice = prompt(edit_prompt)

            # ADD
            if choice['option'] == "Add module":
                # Namespace selection
                ns_prompt = [
                    {
                        'type': 'list',
                        'name': 'namespace',
                        'message': 'Select a namespace for your module',
                        'choices': list(self.modules.keys()) + ["new"],
                    }
                ]
                # Module details
                mod_ns = prompt(ns_prompt)['namespace']
                mod_questions = [
                    {
                        'type': 'input',
                        'name': 'mod_name',
                        'message': 'Name of your module',
                        'validate': ModuleNameValidation,
                    },
                    {
                        'type': 'input',
                        'name': 'mod_desc',
                        'message': 'Module description',
                    },
                    {
                        'type': 'input',
                        'name': 'mod_cmd',
                        'message': 'Command',
                    },
                    {
                        'type': 'confirm',
                        'name': 'mod_su',
                        'message': 'Does this command requires superuser?',
                    }
                ]
                if mod_ns == "new":
                    mod_question = [{
                        'type': 'input',
                        'name': 'mod_ns',
                        'message': 'Name of your namespace',
                        'validate': NamespaceValidation
                    }]
                    mod_namespace = prompt(mod_question)
                try:
                    mod_ns = mod_namespace['mod_ns']
                except:
                    pass
                # Assigning property to the ModuleNameValidation class to 
                # access modules within the selected namespace.
                ModuleNameValidation.modules = self.modules[mod_ns].keys() \
                    if mod_ns in self.modules.keys() else []
                mod_details = prompt(mod_questions)
                mod_dict = {
                        "name": mod_details['mod_name'].title(),
                        "desc": mod_details['mod_desc'],
                        "command":  mod_details['mod_cmd'],
                        "require_superuser": mod_details['mod_su'],
                        "target_os": "win" if check_os() else "linux"
                        }
                try:
                    data[mod_ns.lower()].append(mod_dict)
                except:
                    data.update({mod_ns.lower(): [mod_dict]})
                # Write the updated modules.json
                save_mod_json(data)
                logger.info("Module added successfully. Use 'list' " + \
                    "command to see available modules.")

            # EDIT & REMOVE
            elif choice['option'] == "Edit module" or choice['option'] == "Remove module":
                mod_option = choice['option'].split(" ")[0].lower()
                # Namespace selection
                ns_prompt = [
                    {
                        'type': 'list',
                        'name': 'namespace',
                        'message': "Select the namespace of module to " + mod_option,
                        'choices': list(self.modules.keys())
                    }
                ]
                selected_ns = prompt(ns_prompt)['namespace']
                # Module selection
                mod_prompt = [
                    {
                        'type': 'list',
                        'name': 'module',
                        'message': "Select a module to " + mod_option,
                        'choices': self.modules[selected_ns]
                    }
                ]
                selected_mod = prompt(mod_prompt)['module']
                mod_list = [mod['name'] for mod in list(data[selected_ns])]
                mod_index = mod_list.index(selected_mod)

                # EDIT
                if mod_option == "edit":
                    # Create a list for properties
                    prop_list = list(self.modules[selected_ns][selected_mod].kwargs.keys())
                    prop_list.remove('namespace')
                    prop_list.remove('target_os')
                    # Module property selection
                    prop_prompt = [
                        {
                            'type': 'list',
                            'name': 'property',
                            'message': "Select a property for editing " + selected_mod,
                            'choices': prop_list
                        }
                    ]
                    selected_prop = prompt(prop_prompt)['property']
                    # New value for property
                    new_val = prompt([{
                        'type': 'input',
                        'name': 'val',
                        'message': "New value for " + selected_prop}])['val']
                    new_val = new_val.title() if selected_prop == "name" else new_val
                    # Update the selected property of module
                    data[selected_ns][mod_index][selected_prop] = new_val
                    # Write the updated modules.json
                    save_mod_json(data)
                    logger.info("Module updated successfully. (" + selected_ns + "/" +
                        selected_mod + ":" + selected_prop + ")")

                # REMOVE
                else:
                    data[selected_ns].pop(mod_index)
                    save_mod_json(data)
                    logger.info("Module removed successfully. (" + selected_mod + ")")
            else:
                pass
        except Exception as e:
            logger.error(str(e))
        self.namespace = ""
        self.module = ""
        self.modules = get_modules()

    def do_preset(self, arg):
        """Show/execute the hardening module presets"""
        
        presets = get_presets()
        if arg:
            modules = [preset['modules'] for preset in presets \
                if preset['name'] == arg]
            if len(modules) == 0:
                logger.error(f"Preset not found: '{arg}'")
                return
            modules = modules[0]
            confirm_prompt = [
                {
                    'type': 'confirm',
                    'name': 'confirm',
                    'message': 'Run modules without confirmation?',
                }
            ]
            try:
                conf_mod = prompt(confirm_prompt)['confirm']
            except:
                return
            # Main module loop
            for module in modules:
                # Select the namespace
                self.namespace = module.split("/")[0].lower()
                # Loop through the modules
                for name, mod in self.modules[self.namespace].items():
                    # Select the module if it equals to the module in
                    # the preset or equals to 'all'
                    if module.split("/")[1].lower() == "all" or \
                     module.split("/")[1].lower() == name.lower():
                        # Select the module
                        self.module = str(mod)
                        # Show module information
                        self.do_info(None)
                        # If confirmation not needed
                        if conf_mod:
                            self.do_harden(None)
                        else:
                            # Ask for permission for executing the command
                            exec_conf = prompt([{
                                    'type': 'confirm',
                                    'name': 'confirm',
                                    'message': 'Execute the hardening command?',
                            }])
                            # Execute the command or cancel
                            try:
                                if exec_conf['confirm']:
                                    self.do_harden(None)
                                else:
                                    raise Exception("Cancelled by user.")
                            except:
                                logger.info("Hardening cancelled. " + \
                                f"({self.namespace}/{self.module})")
            # Go back from the selected module and namespace
            self.module = ""
            self.namespace = ""
        else:
            if not presets:
                logger.warn(f"No presets found in {mod_json_file}")
                return
            search_table = [['Preset', 'Modules']]
            table = AsciiTable(search_table)
            max_width = table.column_max_width(1)
            # Create a table of presets
            for preset in presets:
                mods = ""
                for module in preset['modules'][:-1]:
                    mods += '\n'.join(textwrap.wrap(module, max_width - 40)) + '\n'
                mods += '\n'.join(textwrap.wrap(preset['modules'][-1], max_width-40))
                table.table_data.append([preset['name'], mods])
            # Show the table
            if len(table.table_data) > 1:
                print(table.table)
            else:
                logger.warn(f"No presets found in {mod_json_file}")
            
    def complete_preset(self, text, line, begidx, endidx):
        """Complete preset command"""

        avb_presets = [i['name'].lower() for i in get_presets()]
        mline = line.lower().partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:].title() for s in avb_presets if s.startswith(mline)]

    def do_web(self, arg):
        """Start the grapheneX web server"""

        from graphenex.core.web import run_server, app
        app.config['ACCESS_TOKEN'] = secrets.token_urlsafe(6)
        run_server({"host_port":arg} if arg else None, False)

    def do_harden(self, arg):
        """Execute the hardening command"""

        if not (self.module and self.namespace):
            logger.error('Select a module/namespace.')
        else:
            try:
                hrd = self.modules[self.namespace][self.module]
                out = hrd.execute_command()
                print(out)
                logger.info("Hardening command executed successfully.")
            except PermissionError:
                err_msg = "Insufficient permissions for hardening."
                if check_os():
                    err_msg += " Get admin rights and rerun the grapheneX."
                else:
                    err_msg += " Try running the grapheneX with sudo."
                logger.error(err_msg)
            except Exception as e:
                logger.error("Failed to execute hardening command. " + str(e))

    def do_exit(self, arg):
        "Exit interactive shell"

        exit_msgs = [
            "Bye!",
            "Hope to see you soon!",
            "Take care!",
            "I am not going to miss you!",
            "Gonna miss you!",
            "Thank God, you're leaving. What a relief!",
            "Fare thee well!",
            "Farewell, boss.",
            "Daha karpuz kesecektik.",
            "Bon voyage!",
            "Regards.",
            "Exiting..."]
        logger.info(random.choice(exit_msgs))
        return True

    def do_EOF(self, arg):
        """EOF exit"""

        print()
        self.do_exit(arg)
        return True

    def do_clear(self, arg):
        """Clear the terminal"""

        os.system("cls" if check_os() else "clear")

    def default(self, line):
        """Default command"""

        logger.error("Command not found.")

class ModuleNameValidation(Validator):
        def validate(self, document):
            """Validate the module name for the prompt"""

            if not re.match(r'^\w+$', document.text):
                raise ValidationError(
                    message='Enter a valid module name',
                    cursor_position=len(document.text))
            elif document.text.lower() in [module.lower() for module in self.modules]:
                raise ValidationError(
                    message="Try a different name, this module name is not available.",
                    cursor_position=len(document.text))

class NamespaceValidation(Validator):
    def validate(self, document):
        """Validate the namespace for the prompt"""

        namespaces = get_forbidden_namespaces()
        if document.text.lower() in [namespace.lower() for namespace in namespaces]:
            raise ValidationError(
                    message="You do not have permission to access this namespace.",
                    cursor_position=len(document.text))
