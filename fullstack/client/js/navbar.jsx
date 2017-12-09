import React, { Component } from 'react'
import { Link } from 'react-router-dom'

export default class NavBar extends Component {
  render(){
    return(
      <nav className="navbar navbar-default navbar-static-top" role="navigation">
        <div className="navbar-header">
          <div className="container">
            <div className="collapse navbar-collapse">
                <div className="btn-toolbar pull-left navbar-left" role="toolbar">
                  <Link to='/'>
                  <button type="button" className="btn navbar-btn btn-default">
                    <span className="glyphicon glyphicon-home"></span> Navigate
                  </button>
                  </Link>
                </div>

              <div className="btn-toolbar pull-right navbar-right" role="toolbar">
                  <Link to='/about'>
                  <button type="button" className="btn navbar-btn btn-default">
                    <span className="glyphicon glyphicon-info-sign"></span> About
                  </button>
                  </Link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    )
  }
}
