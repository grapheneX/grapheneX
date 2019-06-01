#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.helpers import check_os, get_modules, mod_json_file
from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from terminaltables import AsciiTable
import inquirer
import random
import json
import os
import re

logger = GraphenexLogger(__name__)


class ShellCommands(Help):
    def do_switch(self, arg):
        """Switch between modules or namespaces"""

        if arg:
            arg = arg.lower()
            if arg in self.modules.keys():
                logger.info(f"Switched to \"{arg}\" namespace." +
                            " Use 'list' to see available modules.")
                self.namespace = arg
                self.module = ""
            else:
                self.do_use(arg)
        else:
            logger.warn("'switch' command takes 1 argument.")

    def complete_switch(self, text, line, begidx, endidx):
        """Complete switch command"""

        avb_namespaces = [i.lower() for i in self.modules.keys()]
        mline = line.lower().partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in avb_namespaces if s.startswith(mline)]

    def do_use(self, arg):
        """Use hardening module"""

        if "/" in arg and arg.split("/")[0].lower() in self.modules.keys():
            self.namespace = arg.split("/")[0].lower()
            arg = arg.split("/")[1]

        def select_module_msg():
            logger.info(f"\"{self.module}\" module selected. Use 'harden' command " +
                        "for hardening or use 'info' for more information.")
        if arg:
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
        else:
            logger.warn("'use' command takes 1 argument.")

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
            # case sensitivity
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
        """Information about the desired module"""
        
        if self.module:
            module = self.modules[self.namespace][self.module]

            print(f"\n\tNamespace: {self.namespace}\n\tModule: {module.name}\n\t" + 
                f"Description: {module.desc}\n" + f"\tCommand: {module.command}\n")
        else:
            logger.error('No module selected.')

    def do_search(self, arg):
        """Search for modules"""

        search_table = [['Module', 'Description']]
        if arg:
            if arg in self.modules.keys():
                for name, module in self.modules[arg].items():
                    search_table.append(
                        [arg + "/" + name, module.desc])
            else:
                for k, v in self.modules.items():
                    for name, module in v.items():
                        if arg.lower() in name.lower():
                            search_table.append(
                                [k + "/" + name, module.desc])
            if len(search_table) > 1:
                print(AsciiTable(search_table).table)
            else:
                logger.error(f"Nothing found for \"{arg}\".")
        else:
            self.do_list(None)

    def do_list(self, arg):
        """List available hardening modules"""

        modules_table = [['Module', 'Description']]
        if self.namespace:
            for name, module in self.modules[self.namespace].items():
                modules_table.append([name, module.desc])
        else:
            for k, v in self.modules.items():
                for name, module in v.items():
                    modules_table.append(
                        [k + "/" + name, module.desc])
        print(AsciiTable(modules_table).table)

    def do_back(self, arg):
        """Go back if namespace (hardening method) selected or switched"""

        if self.module:
            self.module = ""
        else:
            self.namespace = ""

    def do_edit(self, arg):
        """Add, edit or delete module"""

        try:
            edit_prompt = [
                inquirer.List('option',
                            message="What do you want to do?",
                            choices=["Add module", "Edit module", "Remove module"],
                        ),
            ]
            choice = inquirer.prompt(edit_prompt)
            # ADD
            if choice['option'] == "Add module":
                # Namespace selection
                ns_prompt = [
                    inquirer.List('namespace',
                                message="Select a namespace for your module",
                                choices=list(self.modules.keys()) + ["new"],
                            ),
                ]
                # Module details
                mod_ns = inquirer.prompt(ns_prompt)['namespace']
                mod_questions = [
                    inquirer.Text('mod_name', message="Name of your module",
                        validate=lambda _, x: re.match(r'^\w+$', x)),
                    inquirer.Text('mod_desc', message="Module description"),
                    inquirer.Text('mod_cmd', message="Command"),
                    inquirer.Confirm('mod_su', message="Does this command requires superuser?",
                    )
                ]
                if mod_ns == "new":
                    mod_questions = [inquirer.Text('mod_ns', message="Name of your namespace")] + mod_questions
                mod_details = inquirer.prompt(mod_questions)
                try:
                    mod_ns = mod_details['mod_ns']
                except:
                    pass
                # Read modules.json
                with open(mod_json_file, 'r') as f:
                    data = json.load(f)
                # Append with other module information
                mod_dict = {
                        "name": mod_details['mod_name'].capitalize(),
                        "desc": mod_details['mod_desc'],
                        "command":  mod_details['mod_cmd'],
                        "require_superuser": mod_details['mod_su'],
                        "target_os": "win" if check_os() else "linux"
                        }
                try:
                    data[mod_ns].append(mod_dict)
                except:
                    data.update({mod_ns: [mod_dict]})
                # Write the updated modules.json
                with open(mod_json_file, 'w') as f:
                    json.dump(data, f)
                self.modules = get_modules()
                logger.info("Module added successfully. Use 'list' command to see available modules.")
            # EDIT
            elif choice['option'] == "Edit module":
                
                ns_prompt = [
                    inquirer.List('namespace',
                                message="Select the namespace of module to edit",
                                choices=list(self.modules.keys()),
                            ),
                ]
                selected_ns = inquirer.prompt(ns_prompt)['namespace']
                mod_prompt = [
                    inquirer.List('module',
                                message="Select a module to edit",
                                choices=list(self.modules[selected_ns]),
                            ),
                ]
                selected_mod = inquirer.prompt(mod_prompt)['module']
                print(self.modules[selected_ns][selected_mod])
                prop_prompt = [
                    inquirer.List('property',
                                message="Select a property for editing " + selected_mod,
                                choices=list(self.modules[selected_ns][selected_mod]),
                            ),
                ]
                selected_prop = inquirer.prompt(prop_prompt)['property']
                

                
            elif choice['option'] == "Remove module":
                # TODO : Implement remove
                pass
            else:
                pass
        except Exception as e:
            logger.error(str(e))
        except KeyboardInterrupt:
            print()
            logger.info("Cancelled by user.")

    def do_web(self, arg):
        """Run the grapheneX web server"""

        from core.web import run_server
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
        """Clear terminal"""

        os.system("cls" if check_os() else "clear")

    def default(self, line):
        """Default command"""

        logger.error("Command not found.")
