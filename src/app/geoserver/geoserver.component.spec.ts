import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GeoserverComponent } from './geoserver.component';

describe('GeouserformComponent', () => {
  let component: GeoserverComponent;
  let fixture: ComponentFixture<GeoserverComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GeoserverComponent]
    });
    fixture = TestBed.createComponent(GeoserverComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
