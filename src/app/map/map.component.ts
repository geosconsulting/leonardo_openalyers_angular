import { Component, OnInit } from '@angular/core';
import Map from 'ol/Map';
import View from 'ol/View';
import {FullScreen, defaults as defaultControls,ZoomSlider} from 'ol/control.js';
import Zoom from 'ol/control/Zoom.js';
import { OSM } from 'ol/source';

import TileLayer from 'ol/layer/Tile';@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})

export class MapComponent implements OnInit {

  public map!: Map
  //zoomSlider = new ZoomSlider();

  ngOnInit(): void {
    this.map = new Map({
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
    ],
    controls: [new FullScreen, new ZoomSlider, new Zoom],
    target: 'map',
    view: new View({
      center: [1373541.5859136516, 5126556.34249262],
      zoom: 9,
      maxZoom: 18,
    }),
  });
 }
 //map.addControl(zoomSlider);
}

