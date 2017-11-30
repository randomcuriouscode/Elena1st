import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import MapComponent from "./mapcomponent";

const MOUNT_NODE = document.getElementById('app')

const render = () => {
  const Navigator = require('./Navigator').default
  ReactDOM.render(<Navigator />, MOUNT_NODE)
}

render()

if (module.hot) {
  module.hot.accept(['./components/navigator'], () =>
    setImmediate(() => {
      ReactDOM.unmountComponentAtNode(MOUNT_NODE)
      render()
    }),
  )
}
