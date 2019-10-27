import React from "react";
import axios from "axios";
import { Collapse, Form, Button } from "react-bootstrap";
import Swal from "sweetalert2";

class ModuleBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
      rotateClass: "",
      hardenRotateClass: "",
      out: this.props.moduleData.source
    };
  }

  hardenApiCall() {
    const { moduleData } = this.props;
    this.setState({
      hardenRotateClass: "rotate_cogs"
    });
    axios
      .post("/api/harden", { module_name: moduleData.name })
      .then(res => {
        const { status, msg, stdout } = res.data;
        if (status) {
          Swal.fire({
            background: "#1E1E1E",
            type: "success",
            confirmButtonColor: "transparent",
            html: `<p style="color: #E0E0E0">${msg}</p>`
          });
          this.setState({
            out: this.state.out + stdout
          });
        } else {
          Swal.fire({
            background: "#1E1E1E",
            type: "error",
            confirmButtonColor: "transparent",
            html: `<p style="color: #E0E0E0">${msg}</p>`
          });
        }
      })
      .catch(err => {
        console.log(err);
      })
      .finally(() => {
        this.setState({
          hardenRotateClass: ""
        });
      });
  }

  render() {
    const { moduleData } = this.props;
    return (
      <div className="module-box deep" style={{ marginBottom: 20 }}>
        <div className="d-flex justify-content-between align-middle p-2">
          <div className="text-left">
            <h6 style={{ marginBottom: 0, wordBreak: "break-all" }}>
              {moduleData.name}
            </h6>
            <p
              className="text-muted"
              style={{ marginBottom: 0, marginTop: 10, fontSize: 13 }}
            >
              {moduleData.desc}
            </p>
          </div>
          <a>
            <i
              style={{ fontSize: 52 }}
              className={"fas fa-arrow-circle-right " + this.state.rotateClass}
              onClick={e => {
                this.setState({
                  isOpen: !this.state.isOpen,
                  rotateClass: !this.state.isOpen ? "rotated" : ""
                });
              }}
            ></i>
          </a>
        </div>
        <Collapse in={this.state.isOpen}>
          <div>
            <Form
              className="logs consolas font-small text-muted"
              as="textarea"
              rows="5"
              cols="30"
              value={"[#]: " + this.state.out}
              disabled
            ></Form>
            <Button
              style={{ backgroundColor: "transparent", borderWidth: 0 }}
              onClick={() => {
                this.hardenApiCall();
              }}
              block
            >
              Run
              <i
                className={"fas fa-cog ml-1 " + this.state.hardenRotateClass}
              ></i>
            </Button>
          </div>
        </Collapse>
      </div>
    );
  }
}

export default ModuleBox;
