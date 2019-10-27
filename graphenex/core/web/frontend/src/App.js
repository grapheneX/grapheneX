import React, { Component } from "react";
import LeftSide from "./Components/LeftSide";
import RightSide from "./Components/RightSide";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="container text-center mt-4 mb-4">
        <div className="row">
          <div className="col-md-4">
            <LeftSide />
          </div>
          <div className="col-md-8">
            <RightSide />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
