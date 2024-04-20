import { Component, OnInit } from "@angular/core";
import { DataService } from "./data.service";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
})
export class AppComponent implements OnInit {
  message = "";

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.fetchData().subscribe({
      next: (data) => {
        this.message = data.message;
      },
      error: (err) => {
        console.error("Failed to fetch data:", err);
      },
    });
  }
}
