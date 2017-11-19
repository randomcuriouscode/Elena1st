import React, { Component } from 'react'
import { Map, TileLayer, Marker, Popup } from 'react-leaflet'

export default class MapPiece extends Component {
  constructor(props){
    super(props)
  this.state = {
    animate: false,
    latlng: {
      lat: 51.505,
      lng: -0.09,
    },
  }


  this.handleClick = e => {
    this.setState({
      latlng: e.latlng,
    })
  }

  this.toggleAnimate = () => {
    this.setState({
      animate: !this.state.animate,
    })
  }
}

  render() {
    const marker = this.state.hasLocation ? (
      <Marker position={this.state.latlng}>
        <Popup>
          <span>You are here</span>
        </Popup>
      </Marker>
    ) : null

    return (
      <div style={{ textAlign: 'center' }}>
        <label>
          <input
            checked={this.state.animate}
            onChange={this.toggleAnimate}
            type="checkbox"
          />
          Animate panning
        </label>
        <Map
          animate={this.state.animate}
          center={this.state.latlng}
          length={4}
          onClick={this.handleClick}
          zoom={13}>
          <TileLayer
            attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {marker}
        </Map>
      </div>
    )
  }
}
