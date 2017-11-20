import React, { Component } from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";
import MapPiece from "./mapcomponent";
import Leaflet from 'leaflet';

require('../css/fullstack.css');
var $ = require('jquery');

Leaflet.Icon.Default.imagePath =
  '//cdnjs.cloudflare.com/ajax/libs/leaflet/1.2.0/images/'



export default class App extends Component {
  constructor(props){
    super(props)
    this.state = {
      editfrom: true,
      fromlatlng: {
        lat: 51.505,
        lng: -0.09,
      },
      tolatlng: {
        lat: 51.505,
        lng: -0.09,
      },
      centerlatlng: {
        lat: 51.505,
        lng: -0.09,
      },
    }


  this.handleMapClick = e => {
    if(this.state.editfrom){
      this.setState({
        editfrom: false,
        fromlatlng: e.latlng,
      })
    }
    else{
      this.setState({
        editfrom: true,
        tolatlng: e.latlng,
      })
    }
  }

}

  render(){
      return(
        <div>
        <h2>Proof of concept for map rendering:</h2>
        <p>Will update with more functionality and styling.</p>
        <p>from latitude: {this.state.fromlatlng.lat}</p>
        <p>from longitude: {this.state.fromlatlng.lng}</p>
        <p>to latitude: {this.state.tolatlng.lat}</p>
        <p>to longitude: {this.state.tolatlng.lng}</p>
        <MapPiece mapClick={this.handleMapClick.bind(this)} fromMarker={this.state.fromlatlng} toMarker={this.state.tolatlng}/>
      </div>
    )
  }
}
