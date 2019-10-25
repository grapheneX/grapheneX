import React, { Component } from "react";
import axios from "axios";
import $ from "jquery";
import { Collapse } from "react-bootstrap";

class LeftSide extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      general: {
        osName: "",
        processor: ""
      },
      disks: [],
      network: [],

      collapseOpen: false
    };
  }

  componentDidMount() {
    axios
      .get("/api/getsysteminfo")
      .then(res => {
        const { general } = res.data;
        this.setState({
          general: {
            osName: general[0],
            processor: general[1]
          }
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div className="box deep">
        <div className="row">
          <div className="col col-md-12">
            <img
              src="static/images/graphenex_logo_white.png"
              alt="logo"
              className="img-responsive"
              height="200"
              width="200"
            />
          </div>
          <div className="col col-md-12">
            <h2>grapheneX</h2>
            <p className="text-muted consolas">
              ~ Automated System Hardening Framework.
              <br />
              + Created for Linux & Windows.
              <br />>
              <a href=" https://github.com/grapheneX" target="_blank">
                https://github.com/grapheneX
              </a>
              <br />- Copyright (C) 2019
            </p>
          </div>
        </div>
        {/* System information */}
        <div className="text-left">
          <ul
            className="text-left"
            style={{ listStyle: "none", padding: 0, margin: 0 }}
          >
            <li id="os">
              <b>OS: </b>
              <span className="text-muted">{this.state.general.osName}</span>
            </li>
            <li id="proc">
              <b>Processor: </b>
              <span className="text-muted">{this.state.general.processor}</span>
            </li>
          </ul>
        </div>
        {/* System information end */}

        <button
          className="btn btn-block d-lg-none opensystembtn"
          style={{ borderWidth: 0, marginTop: 1 }}
          data-toggle="collapse"
          data-target="#systemdiv"
          aria-expanded="false"
          aria-controls="systemdiv"
          onClick={() => {
            if (!this.state.collapseOpen) {
              $(".opensystembtn i").addClass("rotate_arrow");
            } else {
              $(".opensystembtn i").removeClass("rotate_arrow");
            }
            this.setState({ collapseOpen: !this.state.collapseOpen });
          }}
        >
          <i className="fas fa-chevron-down" style={{ fontSize: 24 }}></i>
        </button>
        <Collapse in={this.state.collapseOpen}>
          <div id="systemdiv">afljashdkjasnlasndkjasndkjandaskjd</div>
        </Collapse>
      </div>
    );
  }
}

export default LeftSide;
