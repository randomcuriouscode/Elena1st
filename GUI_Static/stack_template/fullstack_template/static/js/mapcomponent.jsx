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
    this.props.mapClick(e)
  }


}

  render() {
    return (
      <div style={{ textAlign: 'center' }}>
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
          <Marker
            draggable={false}
            position={[this.props.fromMarker.lat,this.props.fromMarker.lng]}
            ref="from here">
            <Popup minWidth={90}>
            </Popup>
          </Marker>
          <Marker
            draggable={false}
            position={[this.props.toMarker.lat,this.props.toMarker.lng]}
            ref="to here">
            <Popup minWidth={90}>
            </Popup>
          </Marker>

        </Map>
      </div>
    )
  }
}
