import React from "react";
import axios from "axios";
import {
  Dropdown,
  InputGroup,
  FormControl,
  Button,
  Form
} from "react-bootstrap";
import { Container, Button as FloatButton } from "react-floating-action-button";
import ModuleBox from "./ModuleBox";
import NamespaceSelector from "./NamespaceSelector";
import GraphenexLogo from "../Loading";
import _Swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";

const Swal = withReactContent(_Swal);

class RightSide extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      selectedNamespace: "",
      namespaces: [],
      modules: [],
      searchQuery: "",

      namespaceForAdd: "",
      superUserPriv: false
    };

    this.handleSearch = this.handleSearch.bind(this);
  }

  componentDidMount() {
    this.getNamespacesAndModules();
  }

  getNamespacesAndModules() {
    axios
      .get("/api/getnamespaces")
      .then(res => {
        this.setState({
          namespaces: res.data,
          selectedNamespace: res.data[0]
        });
        this.getModules(res.data[0]);
      })
      .catch(err => {
        console.log(err);
      });
  }
  getModules(namespace) {
    axios
      .post("/api/getmodules", { namespace })
      .then(res => {
        this.setState({
          modules: res.data,
          isLoading: false
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  changeNamespace(namespace) {
    this.setState({
      selectedNamespace: namespace
    });
    this.getModules(namespace);
  }

  searchApiCall(string) {
    axios
      .post("/api/search", { query: string })
      .then(res => {
        const { result } = res.data;
        this.setState({
          modules: result
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  addModuleApiCall(moduleObj) {
    axios
      .post("/api/addmodule", { moduleObj })
      .then(res => {
        const { data } = res;
        if (data.status) {
          Swal.fire({
            type: "success",
            text: data.msg
          });
        } else {
          Swal.fire({
            type: "error",
            text: data.msg
          });
        }
      })
      .catch(err => {
        console.log(err);
      })
      .finally(() => {
        this.getNamespacesAndModules();
      });
  }

  handleSearch(e) {
    this.searchApiCall(e.target.value);
    this.setState({
      searchQuery: e.target.value
    });
  }

  namespaceForAddHandler(namespace) {
    this.setState({
      namespaceForAdd: namespace
    });
  }

  render() {
    return (
      <div>
        <div className="d-flex justify-content-between mt-sm-0 mt-3">
          <h5 className="flex-grow-1 text-left">Available Modules</h5>
          <Dropdown>
            <Dropdown.Toggle className="deep" variant="outline-dark">
              {this.state.selectedNamespace}
            </Dropdown.Toggle>
            <Dropdown.Menu>
              {this.state.namespaces.map((namespace, index) => (
                <Dropdown.Item
                  key={index}
                  onClick={() => this.changeNamespace(namespace)}
                >
                  {namespace}
                </Dropdown.Item>
              ))}
            </Dropdown.Menu>
          </Dropdown>
        </div>
        <InputGroup className="my-3">
          <FormControl
            value={this.state.searchQuery}
            placeholder="Search Module"
            onChange={this.handleSearch}
          />
          <InputGroup.Append>
            <Button>
              <i className="fa fa-search"></i>
            </Button>
          </InputGroup.Append>
        </InputGroup>

        {/* Modules */}
        {this.state.isLoading ? (
          <GraphenexLogo />
        ) : (
          this.state.modules.map(moduleData => (
            <ModuleBox moduleData={moduleData} key={moduleData.name} />
          ))
        )}
        <Container styles={{ zIndex: 99 }}>
          <FloatButton
            tooltip="Add module"
            icon="fas fa-plus"
            styles={{
              backgroundColor: "#111111",
              color: "#E0E0E0"
            }}
            onClick={() => {
              Swal.fire({
                customClass: {
                  container: "z-index: 999"
                },
                title: "Add a new module",
                background: "#1E1E1E",
                html: (
                  <Form className="text-left" style={{ color: "#E0E0E0" }}>
                    <Form.Label>Namespace</Form.Label>
                    <NamespaceSelector
                      namespaces={this.state.namespaces}
                      setNamespace={this.namespaceForAddHandler.bind(this)}
                    />
                    <Form.Label>Module Name</Form.Label>
                    <FormControl
                      className="mb-2"
                      type="text"
                      placeholder="Module name"
                      id="moduleName"
                    />
                    <Form.Label>Module Description</Form.Label>
                    <FormControl
                      className="mb-2"
                      as="textarea"
                      rows={5}
                      placeholder="Module Description"
                      id="moduleDesc"
                    />
                    <Form.Label>Module Command</Form.Label>
                    <FormControl
                      className="consolas"
                      as="textarea"
                      rows={5}
                      placeholder="Module Command"
                      id="moduleCommand"
                    />
                    <Form.Check
                      className="mt-2"
                      type="switch"
                      onChange={() => {
                        this.setState({
                          superUserPriv: !this.state.superUserPriv
                        });
                      }}
                      label="Requires Superuser Privileges"
                      id="superuser-switch"
                    />
                  </Form>
                ),
                focusConfirm: false,
                preConfirm: () => {
                  return {
                    namespace: this.state.namespaceForAdd,
                    name: document.getElementById("moduleName").value,
                    desc: document.getElementById("moduleDesc").value,
                    command: document.getElementById("moduleCommand").value,
                    su: this.state.superUserPriv
                  };
                }
              }).then(({ value }) => {
                if (value) {
                  this.addModuleApiCall(value);
                }
              });
            }}
            rotate
          />
        </Container>
      </div>
    );
  }
}

export default RightSide;
