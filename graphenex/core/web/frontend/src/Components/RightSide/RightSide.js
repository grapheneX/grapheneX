import React from "react";
import axios from "axios";
import {
  Container,
  Col,
  Row,
  Dropdown,
  InputGroup,
  FormControl,
  Button,
  Collapse
} from "react-bootstrap";
import ModuleBox from "./ModuleBox";

class RightSide extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedNamespace: "",
      namespaces: [],
      modules: []
    };
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
          modules: res.data
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
          <FormControl placeholder="Search Module" />
          <InputGroup.Append>
            <Button>
              <i className="fa fa-search"></i>
            </Button>
          </InputGroup.Append>
        </InputGroup>

        {/* Modules */}
        <ModuleBox />
      </div>
    );
  }
}

export default RightSide;
