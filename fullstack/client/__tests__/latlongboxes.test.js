import React from 'react';
import { mount, configure } from 'enzyme';
import LatLongForm from '../js/latlongboxes';
import Adapter from 'enzyme-adapter-react-16';


configure({ adapter: new Adapter() });

describe("LatLongForm", () => {
  let props;
  let mountedForm;

  let pathDist = 15;
  let pathElev = 20;
  let beginEditTo = ()=>{};
  let beginEditFrom = ()=>{};
  let sendToServer = ()=>{};
  let fromlatlng = { lat: 42.389620, lng: -72.528230 };
  let tolatlng = { lat: 42.389620, lng: -72.528230 };
  let flex = 100;
  let elev = 1;

  const latLongForm = () => {
    if (!mountedForm) {

      mountedForm = mount(
        <LatLongForm routeDist={pathDist} routeElev={pathElev} editTo={beginEditTo} editFrom={beginEditFrom} submitCoordinates={sendToServer} initfrom={fromlatlng} initto={tolatlng} initflex={flex} initelev={elev}/>
      );
    }
    return mountedForm;
  }

  beforeEach(() => {
    props = {
      routeDist: undefined,
      routeElev: undefined,
      initflex: undefined,
      initelev: undefined,
    };
    mountedForm = undefined;
  });

  it("always renders a div", () => {
    const divs = latLongForm().find("div");
    expect(divs.length).toBeGreaterThan(0);
  });

  it("always renders a slider", () => {
    const slider = latLongForm().find("ReactBootstrapSlider");
    expect(slider.length).toBeGreaterThan(0);
  });

  it("always renders location buttons", () => {
    const buttons = latLongForm().find("button");
    expect(buttons.length).toBeGreaterThan(1);
  });

  it("always renders full form", () => {
    const inputs = latLongForm().find("input");
    expect(inputs.length).toBeGreaterThan(4);
  });

  it("distance props passed correctly", () => {
    const dist = parseInt(latLongForm().state.distance);
    expect(dist).not.toBeGreaterThan(flex);
    expect(dist).not.toBeLessThan(flex);
  });

  it("elevation props passed correctly", () => {
    const dist = parseInt(latLongForm().state.elevation);
    expect(dist).not.toBeGreaterThan(elev);
    expect(dist).not.toBeLessThan(elev);
  });

  it("from props passed correctly", () => {
    const dist = parseInt(latLongForm().state.fromlat);
    expect(dist).not.toBeGreaterThan(fromlatlng.lat);
    expect(dist).not.toBeLessThan(fromlatlng.lat);
  });


});
