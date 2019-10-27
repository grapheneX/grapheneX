import React from "react";
import { Collapse } from "react-bootstrap";

class ModuleBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isOpen: false, rotateClass: "" };
  }

  render() {
    return (
      <div className="module-box deep">
        <div className="d-flex justify-content-between align-middle p-2">
          <div className="text-left">
            <h6 style={{ marginBottom: 0, wordBreak: "break-all" }}>
              Disable_File_Sharing
            </h6>
            <p
              className="text-muted"
              style={{ marginBottom: 0, marginTop: 10, fontSize: 13 }}
            >
              Disable File and Printer Sharing.
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
            <p>asdasd</p>
          </div>
        </Collapse>
      </div>
    );
  }
}

export default ModuleBox;
