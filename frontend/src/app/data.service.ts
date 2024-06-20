import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private baseUrl = 'http://backend:5100/api';

  constructor(private http: HttpClient) { }

  fetchData(): Observable<any> {
    const url = `${this.baseUrl}/cs-skins/first`;
    return this.http.get<any>(url);
  }
}
