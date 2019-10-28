import React from "react";

class GraphenexLoading extends React.PureComponent {
  render() {
    return (
      <div className="overlay text-center">
        <img
          className="img-responsive align-middle loading-img"
          src="static/images/graphenex_logo_white.png"
          alt="loading-logo"
          height="200"
          width="200"
        />
      </div>
    );
  }
}

export default GraphenexLoading;
