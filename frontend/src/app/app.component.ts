import { Component, OnInit } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Component({
  selector: "app-root",
  // template: `<h1>{{ message }}</h1>`,
  templateUrl: "./app.component.html",
})
export class AppComponent implements OnInit {
  message = "";

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http
      .get<{ message: string }>("http://backend:5100/api/data") // Update URL to use service name 'backend'
      .subscribe((data) => {
        this.message = data.message;
      });
  }
}
