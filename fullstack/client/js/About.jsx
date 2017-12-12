import React, { Component } from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";
import MapPiece from "./mapcomponent";
import Leaflet from 'leaflet';
import NavBar from './navbar';
import LatLongForm from './latlongboxes';

require('../css/fullstack.css');
var $ = require('jquery');


var $ = require('jquery');

export default class About extends Component {
  render(){
      return(
        <div className="row">
            <div className="col-md-6 col-md-offset-3">
              This is EleNa, an Elevation-based navigation tool! We are Group EleNa#1 from CS520. This tool can be used to find the shortest route, within X% of the actual shortest route, which minimizes or maximizes elevation gain. Please use the tool on the main page to do so!
            </div>
        </div>
    )
  }
}
