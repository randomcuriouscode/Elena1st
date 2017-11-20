import React, { Component } from 'react'

export default class NavBar extends Component {
  render(){
    return(
      <nav className="navbar navbar-default navbar-static-top" role="navigation">
        <div className="navbar-header">
          <div className="container">
            <div className="collapse navbar-collapse">
                <div className="btn-toolbar pull-left navbar-left" role="toolbar">
                  <button type="button" className="btn navbar-btn btn-default">
                    <span className="glyphicon glyphicon-home"></span> Navigate
                  </button>
                </div>

              <div className="btn-toolbar pull-right navbar-right" role="toolbar">
                  <button type="button" className="btn navbar-btn btn-default">
                    <span className="glyphicon glyphicon-info-sign"></span> About
                  </button>
              </div>
            </div>
          </div>
        </div>
      </nav>
    )
  }
}
