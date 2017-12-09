import React, { Component } from "react";
import { PageHeader } from "react-bootstrap";
import { Switch, Route } from 'react-router-dom'
import NavBar from './navbar';
import App from './App';
import About from './About';
import { BrowserRouter } from 'react-router-dom'


require('../css/fullstack.css');
var $ = require('jquery');

var $ = require('jquery');

export default class Navigator extends Component {
  render(){
      return(
        <BrowserRouter>
        <div>
          <NavBar />
          <Switch>
            <Route exact path='/' component={App}/>
            <Route path='/about' component={About}/>
          </Switch>
        </div>
        </BrowserRouter>
    )
  }
}
