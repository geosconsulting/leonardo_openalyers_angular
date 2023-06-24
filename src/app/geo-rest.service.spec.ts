import { TestBed } from '@angular/core/testing';

import { GeoRestService } from './geo-rest.service';

describe('GeoRestService', () => {
  let service: GeoRestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GeoRestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
