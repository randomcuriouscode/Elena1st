import React from 'react';
import { mount, configure } from 'enzyme';
import MapPiece from '../js/mapcomponent';
import Adapter from 'enzyme-adapter-react-16';


configure({ adapter: new Adapter() });

describe("LatLongForm", () => {
  let props;
  let mountedMap;


  let handleMapClick = ()=>{};
  let fromlatlng = { lat: 42.389620, lng: -72.528230 };
  let tolatlng = { lat: 42.389620, lng: -72.528230 };
  let testRoute;
  const Map = () => {
    if (!mountedMap) {

      mountedMap = mount(
        <MapPiece mapClick={handleMapClick()} fromMarker={fromlatlng} toMarker={tolatlng} bestRoute={testRoute} />
      );
    }
    return mountedMap;
  }

  beforeEach(() => {
    props = {
      fromMarker: null,
      toMarker: null,
      bestRoute: null,
    };
    mountedMap = undefined;
  });

  it("always renders a div", () => {
    const divs = Map().find("div");
    expect(divs.length).toBeGreaterThan(0);
  });

  it("does not render a route if one is not given", () => {
    const routes = Map().find("Polyline");
    expect(routes.length).not.toBeGreaterThan(0);
  });

  it("always renders a Map correctly", () => {
    const maps = Map().find("Map");
    expect(maps.length).toBeGreaterThan(0);
  });

});
