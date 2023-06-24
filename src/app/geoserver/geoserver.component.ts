import { Component } from '@angular/core';
import { GeoRestService } from '../geo-rest.service';
import { Layers } from '../shared/layers';


@Component({
  selector: 'app-geoserver',
  templateUrl: './geoserver.component.html',
  styleUrls: ['./geoserver.component.css']
})
export class GeoserverComponent {

  geoserver_users = ['fabiolana', 'topp', 'sf'];
  selectedUser = this.geoserver_users[0];
  layers : Layers[] = [];
  value = '';

  constructor(private geoRest:GeoRestService){
    //this.value = this.selectedUser;
  }

  onSelected(value:string){
    this.selectedUser = value;
  }

  getLayers(){
    this.geoRest.getAllLayers().subscribe(
      (res: Layers[]) =>{
        console.log(res);
        this.layers = res;
      },
      (err) => {
        console.error(err);
      },
    )
  }

  onFetchUserLayers(value:string){
    console.log(value);
    this.geoRest.getUserLayers(value).subscribe(
      (res: Layers[]) =>{
        console.log(res);
        this.layers = res;
      },
      (err) => {
        console.error(err);
      },
    )
  }

  onChangeUser(){
    window.alert('USer changed $(this.currentUser}');
  }

  //TODO Adding Workspaces and Styles getters
}
