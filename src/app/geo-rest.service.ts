import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {map, Observable} from 'rxjs';
import {ApiResponse} from "./shared/apiResponse";
import { Layers } from './shared/layers';


@Injectable({
  providedIn: 'root'
})
export class GeoRestService {

  // Base url
  baseurl = 'http://localhost:8000/';

  constructor(private http: HttpClient) {
    this.getAllLayers()
  }

  public getAllLayers(): Observable<Layers[]> {
    let geoserver_layer_rest_url = this.baseurl + 'layers';
    console.log(geoserver_layer_rest_url);
    return this.http.get<Layers[]>(geoserver_layer_rest_url);

    // return this.http.get<ApiResponse>(geoserver_layer_rest_url)
    //   .pipe(
    //       map(response => {
    //         //return response.layers.layer;
    //         return response.layers.layer;
    //       })
    // );
  }

  public getUserLayers(username: string): Observable<Layers[]> {
    let geoserver_layer_rest_url = this.baseurl + 'layers?user_name=' + username;
    console.log(geoserver_layer_rest_url);
    return this.http.get<Layers[]>(geoserver_layer_rest_url);
  }



}
