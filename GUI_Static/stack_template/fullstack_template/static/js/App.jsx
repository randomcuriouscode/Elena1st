import React from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";
import MapPiece from "./mapcomponent";

require('../css/fullstack.css');
var $ = require('jquery');

import HeaderBackgroundImage from '../images/header.jpg';

const App = () => (
  <div>
    <h2>Proof of concept for map rendering:</h2>
    <p>Will update with more functionality and styling.</p>
    <MapPiece />
    </div>
)

export default App
