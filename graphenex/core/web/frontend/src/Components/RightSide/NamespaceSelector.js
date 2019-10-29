import React from "react";
import { ListGroup, FormControl } from "react-bootstrap";

class NamespaceSelector extends React.Component {
  constructor(props) {
    super(props);
    const { namespaces } = props;
    this.state = {
      namespaces: namespaces,
      selectedNamespace: namespaces[0],
      isNew: false,
      newNamespace: ""
    };
    this.handleNewNamespace = this.handleNewNamespace.bind(this);
  }

  handleNewNamespace(e) {
    this.setState({
      newNamespace: e.target.value
    });
  }

  render() {
    const { selectedNamespace, isNew, namespaces, newNamespace } = this.state;
    const { setNamespace } = this.props;
    return (
      <ListGroup>
        {namespaces.map((namespace, index) => (
          <ListGroup.Item
            key={index}
            active={selectedNamespace == namespace}
            onClick={() => {
              this.setState({
                selectedNamespace: namespace
              });
              setNamespace(namespace);
            }}
          >
            {namespace}
          </ListGroup.Item>
        ))}
        {isNew ? (
          <ListGroup.Item style={{ padding: 0 }}>
            <FormControl
              autoFocus
              style={{ margin: 0 }}
              type="text"
              onChange={this.handleNewNamespace}
              onBlur={() => {
                alert("focus out");
              }}
              onKeyPress={target => {
                if (target.charCode == 13) {
                  setNamespace(newNamespace);
                  if (!namespaces.includes(newNamespace)) {
                    namespaces.push(newNamespace);
                  }
                  this.setState({
                    namespaces: namespaces,
                    selectedNamespace: newNamespace,
                    isNew: false
                  });
                }
              }}
            ></FormControl>
          </ListGroup.Item>
        ) : (
          <ListGroup.Item
            onClick={() => {
              this.setState({
                isNew: true
              });
            }}
          >
            <div className="d-flex justify-content-between">
              New Namespace
              <i className="fas fa-plus"></i>
            </div>
          </ListGroup.Item>
        )}
      </ListGroup>
    );
  }
}

export default NamespaceSelector;
