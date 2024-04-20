import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root",
})
export class DataService {
  private backendUrl = "http://backend:5100/api/data";

  constructor(private http: HttpClient) {}

  fetchData(): Observable<{ message: string }> {
    return this.http.get<{ message: string }>(this.backendUrl);
  }
}
