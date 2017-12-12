import React, { Component } from "react";
import ReactBootstrapSlider from 'react-bootstrap-slider';

export default class LatLongForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fromlat: this.props.initfrom.lat,
      fromlng: this.props.initfrom.lng,
      tolat: this.props.initto.lat,
      tolng: this.props.initto.lng,
      distance: 100,
      elevation: 1,
    };

    this.handleFromLatChange = this.handleFromLatChange.bind(this);
    this.handleFromLngChange = this.handleFromLngChange.bind(this);
    this.handleToLatChange = this.handleToLatChange.bind(this);
    this.handleToLngChange = this.handleToLngChange.bind(this);
    this.handleFlexChange = this.handleFlexChange.bind(this);
    this.handleElevChange = this.handleElevChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.renderRouteDetails = this.renderRouteDetails.bind(this);
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      fromlat: nextProps.initfrom.lat,
      fromlng: nextProps.initfrom.lng,
      tolat: nextProps.initto.lat,
      tolng: nextProps.initto.lng,
      elevation: nextProps.initelev,
    })
    if(this.state.distance < 100){
      this.setState({
        distance: nextProps.initflex
      })
    }
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
    this.setState({distance: event.target.value});
  }
  handleElevChange(event){
    this.setState({elevation: event.target.value});
  }

  handleSubmit(event) {
    this.props.submitCoordinates(this.state);
    event.preventDefault();
  }

  renderRouteDetails(){
    if(typeof this.props.routeDist != 'undefined'){
      return(
        <div>
          <u>Route Details:</u><br />
          Distance: {this.props.routeDist}
          <br />
          Elevation Gain: {this.props.routeElev}
        </div>
      );
    }
    else{
      return;
    }
  }

  render() {
    return (
      <div className="row">
          <div className="col-md-6 col-md-offset-3">
      <form className="range input-sm" onSubmit={this.handleSubmit} style={{ padding: '15px'}}>
        <label>
          <table className="input-table">
            <tbody>
            <tr><th>From Latitude:</th><th>From Longitude:</th></tr>
          <tr>
          <th><input className="form-control" type="text" value={this.state.fromlat} onChange={this.handleFromLatChange} /></th>
          <th><input className="form-control" type="text" value={this.state.fromlng} onChange={this.handleFromLngChange} /></th>
          <th><button type="button" className="btn btn-default" onClick={this.props.editFrom}><span className="glyphicon glyphicon-map-marker"></span> Select From</button></th>
          </tr>
          <tr><th>To Latitude:</th><th>To Longitude:</th></tr>
          <tr>
            <th><input className="form-control" type="text" value={this.state.tolat} onChange={this.handleToLatChange} /></th>
            <th><input className="form-control" type="text" value={this.state.tolng} onChange={this.handleToLngChange} /></th>
            <th><button type="button" className="btn btn-default" onClick={this.props.editTo}><span className="glyphicon glyphicon-map-marker"></span> Select To</button></th>
          </tr>
          <tr>
            <th colSpan="3">
            <br />

              <ReactBootstrapSlider
                  value={this.state.distance}
                  slideStop={this.handleFlexChange}
                  step={5}
                  max={1000}
                  min={100}
                   /> &nbsp;&nbsp;&nbsp;&nbsp;{this.state.distance}% Flexibility allowed

            </th>
          </tr>
          <tr>
            <th colSpan="2">
            <br />
              <input type="radio" name="minmax" onClick={this.handleElevChange} value="1" /> Minimize elevation<br />
              <input type="radio" name="minmax" onClick={this.handleElevChange} value="2" /> Maximize elevation<br />
            </th>
            <th>
              {this.renderRouteDetails()}
            </th>
          </tr>
          </tbody>
          </table>
      </label>

        <br />
        <input className="btn btn-default" type="submit" value="Calculate Route" />
      </form>
    </div>
  </div>
    );
  }
}
