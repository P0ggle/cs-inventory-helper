import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';

@Component({
  selector: 'app-show-weapon-details',
  templateUrl: './show-weapon-details.component.html',
  styleUrls: ['./show-weapon-details.component.css'],
})
export class ShowWeaponDetailsComponent implements OnInit {
  weaponDetails: any;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.fetchData().subscribe({
      next: (data) => {
        console.log('Received data: ', data);
        this.weaponDetails = data;
        console.log('Assigned weaponDetails: ', this.weaponDetails);
      },
      error: (err) => {
        console.error('Failed to fetch data:', err);
      },
    });
  }
}
