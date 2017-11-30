import React, { Component } from "react";

export default class LatLongForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fromlat: this.props.initfrom.lat,
      fromlng: this.props.initfrom.lng,
      tolat: this.props.initto.lat,
      tolng: this.props.initto.lng,
      pctflex: this.props.initflex
    };

    this.handleFromLatChange = this.handleFromLatChange.bind(this);
    this.handleFromLngChange = this.handleFromLngChange.bind(this);
    this.handleToLatChange = this.handleToLatChange.bind(this);
    this.handleToLngChange = this.handleToLngChange.bind(this);
    this.handleFlexChange = this.handleFlexChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      fromlat: nextProps.initfrom.lat,
      fromlng: nextProps.initfrom.lng,
      tolat: nextProps.initto.lat,
      tolng: nextProps.initto.lng,
      pctflex: nextProps.initflex
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
  handleFlexChange(event){
    this.setState({pctflex: event.target.value});
  }

  handleSubmit(event) {
    this.props.submitCoordinates(this.state);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit} style={{ padding: '15px' }}>
        <label>
          <table>
            <tbody>
            <tr><th>From Latitude:</th><th>From Longitude:</th></tr>
          <tr>
          <th><input type="text" value={this.state.fromlat} onChange={this.handleFromLatChange} /></th>
          <th><input type="text" value={this.state.fromlng} onChange={this.handleFromLngChange} /></th>
          </tr>
          <tr><th>To Latitude:</th><th>To Longitude:</th></tr>
          <tr>
            <th><input type="text" value={this.state.tolat} onChange={this.handleToLatChange} /></th>
            <th><input type="text" value={this.state.tolng} onChange={this.handleToLngChange} /></th>
          </tr>
          <tr >
            <th colSpan="2">
            <br />
            <input type="range" name="points" min="0" max="100" defaultValue={this.state.pctflex} onChange={this.handleFlexChange} /> {this.state.pctflex}% Distance Flexibility Allowed
            </th>
          </tr>
          </tbody>
          </table>
      </label>

        <br />
        <input type="submit" value="Calculate Route" />
      </form>
    );
  }
}
