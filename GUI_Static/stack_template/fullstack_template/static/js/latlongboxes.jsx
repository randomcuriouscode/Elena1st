import React, { Component } from "react";

export default class LatLongForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fromlat: this.props.initfrom.lat,
      fromlng: this.props.initfrom.lng,
      tolat: this.props.initto.lat,
      tolng: this.props.initto.lng
    };

    this.handleFromLatChange = this.handleFromLatChange.bind(this);
    this.handleFromLngChange = this.handleFromLngChange.bind(this);
    this.handleToLatChange = this.handleToLatChange.bind(this);
    this.handleToLngChange = this.handleToLngChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      fromlat: nextProps.initfrom.lat,
      fromlng: nextProps.initfrom.lng,
      tolat: nextProps.initto.lat,
      tolng: nextProps.initto.lng
    })
  }

  handleFromLatChange(event) {
    this.setState({fromlat: event.target.value});
  }
  handleFromLngChange(event) {
    this.setState({fromlng: event.target.value});
  }
  handleToLatChange(event) {
    this.setState({tolat: event.target.value});
  }
  handleToLngChange(event) {
    this.setState({tolng: event.target.value});
  }

  handleSubmit(event) {
    this.props.submitCoordinates(this.state);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          From Latitude:
          <input type="text" value={this.state.fromlat} onChange={this.handleFromLatChange} />
            From Longitude:
            <input type="text" value={this.state.fromlng} onChange={this.handleFromLngChange} />
            <br />
              To Latitude:
              <input type="text" value={this.state.tolat} onChange={this.handleToLatChange} />
                To Longitude:
                <input type="text" value={this.state.tolng} onChange={this.handleToLngChange} />
        </label>
        <input type="submit" value="Calculate Route" />
      </form>
    );
  }
}
