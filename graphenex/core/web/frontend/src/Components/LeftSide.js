import React, { Component } from "react";
import axios from "axios";
import $ from "jquery";
import { Collapse, ProgressBar, Fade } from "react-bootstrap";
import ContentLoader from "react-content-loader";

const LoadingLine = props => {
  return (
    <ContentLoader
      height={70}
      width={400}
      speed={2}
      primaryColor="#181818"
      secondaryColor="#1E1E1E"
    >
      <rect x="14" y="15" rx="5" ry="5" width="400" height="10" />
      <rect x="14" y="45" rx="5" ry="5" width="400" height="10" />
    </ContentLoader>
  );
};

const DiskLoader = porps => {
  return (
    <ContentLoader
      height={160}
      width={400}
      speed={2}
      primaryColor="#181818"
      secondaryColor="#1E1E1E"
    >
      <rect x="14" y="10" rx="0" ry="0" width="37" height="15" />
      <rect x="14" y="40" rx="5" ry="5" width="400" height="20" />
      <rect x="14" y="70" rx="0" ry="0" width="37" height="15" />
      <rect x="14" y="100" rx="5" ry="5" width="400" height="20" />
    </ContentLoader>
  );
};

const SystemInfo = props => {
  const { info } = props;
  return (
    <ul
      className="text-left"
      style={{ listStyle: "none", padding: 0, margin: 0 }}
    >
      <li id="os" style={{ display: "inline" }}>
        <b>OS: </b>
        <span className="text-muted">{info.osName}</span>
      </li>
      <li id="proc">
        <b>Processor: </b>
        <span className="text-muted">{info.processor}</span>
      </li>
    </ul>
  );
};

const Disk = props => {
  const { disk, key } = props;
  let percent = disk[0][3];
  let variant = null;
  if (percent > 80.0) {
    variant = "danger";
  }
  return (
    <div className="mb-1 text-left" key={key}>
      <h6 style={{ fontSize: 12 }}>{disk[1]}</h6>
      <ProgressBar
        variant={variant}
        now={percent}
        label={`${percent}%`}
        key={key}
      />
    </div>
  );
};

const NetworkTable = props => {
  const { networkData } = props;
  return (
    <div className="table-responsive" style={{ maxHeight: 300 }}>
      <table className="table table-striped table-dark table-borderless text-left">
        <thead>
          <tr>
            <th scope="col">
              Mask <i className="fa fa-mask"></i>
            </th>
            <th scope="col">
              Sent <i className="fa fa-arrow-up"></i>
            </th>
            <th scope="col">
              Recv <i className="fa fa-arrow-down"></i>
            </th>
          </tr>
        </thead>
        <tbody>
          {networkData.map((mask, index) => (
            <NetworkMask mask={mask} key={index} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

const NetworkMask = props => {
  const { mask } = props;
  return (
    <tr id={mask[3]}>
      <th scope="row">{mask[0]}</th>
      <td>{mask[2]}</td>
      <td>{mask[1]}</td>
    </tr>
  );
};

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

      collapseOpen: false,
      isLoading: true
    };
  }

  componentDidMount() {
    axios
      .get("/api/getsysteminfo")
      .then(res => {
        console.log(res);
        const { general, disks, network } = res.data;
        setTimeout(() => {
          this.setState({
            general: {
              osName: general[0],
              processor: general[1]
            },
            disks: disks,
            network: network,
            isLoading: false
          });
        }, 1000);
      })
      .catch(err => {
        console.log(err);
      });
    this.networkInterval = setInterval(() => {
      this.getNetworkData();
    }, 5000);
  }

  componentWillUnmount() {
    clearInterval(this.networkInterval);
  }

  getNetworkData() {
    axios
      .get("/api/getnetwork")
      .then(res => {
        this.setState({
          network: res.data
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
              <br />>{" "}
              <a href=" https://github.com/grapheneX" target="_blank">
                https://github.com/grapheneX
              </a>
              <br />- Copyright (C) 2019
            </p>
          </div>
        </div>
        {/* System information */}
        <div className="text-left">
          <Fade in={!this.state.isLoading}>
            {this.state.isLoading ? (
              <LoadingLine />
            ) : (
              <SystemInfo info={this.state.general} />
            )}
          </Fade>
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
          <div id="systemdiv">
            <div>
              <div className="mb-4 mt-3 text-left">
                <h6>
                  Disks <i className="fas fa-hdd"></i>
                </h6>
                <hr />
                {this.state.isLoading ? (
                  <DiskLoader />
                ) : (
                  this.state.disks.map((disk, index) => (
                    <Disk disk={disk} key={index} />
                  ))
                )}
              </div>
            </div>
            <h6 className="text-left">
              Network <i className="fa fa-network-wired"></i>
            </h6>
            <hr />
            {!this.state.isLoading ? (
              <NetworkTable networkData={this.state.network} />
            ) : (
              <LoadingLine />
            )}
          </div>
        </Collapse>
      </div>
    );
  }
}

export default LeftSide;
