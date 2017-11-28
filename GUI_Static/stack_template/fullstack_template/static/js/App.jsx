import React, { Component } from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";
import MapPiece from "./mapcomponent";
import Leaflet from 'leaflet';
import NavBar from './navbar';
import LatLongForm from './latlongboxes';

require('../css/fullstack.css');
var $ = require('jquery');

Leaflet.Icon.Default.imagePath =
  '//cdnjs.cloudflare.com/ajax/libs/leaflet/1.2.0/images/'

var $ = require('jquery');

export default class App extends Component {
  constructor(props){
    super(props)
    this.state = {
      editfrom: true,
      flex: 25,
      fromlatlng: {
        lat: 42.389620,
        lng: -72.528230,
      },
      tolatlng: {
        lat: 42.389620,
        lng: -72.528230,
      },
      centerlatlng: {
        lat: 42.389620,
        lng: -72.528230,
      },
    }

  this.sendToServer = coords => {
    console.log(coords.fromlat+', '+coords.fromlng);
    console.log(coords.tolat+', '+coords.tolng);
    var tosend = coords;
    tosend["flex"] = coords.pctflex
    $.ajax({
      type: 'GET',
      url: window.location.href + 'route',
      data: tosend,
      dataType: 'json',
      success: (data) => {
        console.log(data);
      }
    });

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
  this
}


  render(){
      return(
        <div>
        <LatLongForm submitCoordinates={this.sendToServer.bind(this)} initfrom={this.state.fromlatlng} initto={this.state.tolatlng} initflex={this.state.flex}/>
        <MapPiece mapClick={this.handleMapClick.bind(this)} fromMarker={this.state.fromlatlng} toMarker={this.state.tolatlng}/>
      </div>
    )
  }
}
