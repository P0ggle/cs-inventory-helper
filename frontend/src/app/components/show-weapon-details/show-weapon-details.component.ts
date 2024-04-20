import { Component, OnInit } from "@angular/core";
import { DataService } from "../../data.service";

@Component({
  selector: "app-show-weapon-details",
  templateUrl: "./show-weapon-details.component.html",
  styleUrl: "./show-weapon-details.component.css",
})
export class ShowWeaponDetailsComponent implements OnInit {
  message = "";

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.fetchData().subscribe({
      next: (data) => {
        this.message = data.message; // Directly assign the object
      },
      error: (err) => {
        console.error("Failed to fetch data:", err);
      },
    });
  }
}
