import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';

@Component({
  selector: 'app-show-weapon-details',
  templateUrl: './show-weapon-details.component.html',
  styleUrls: ['./show-weapon-details.component.css'],
})
export class ShowWeaponDetailsComponent implements OnInit {
  weaponDetails: any;
  imageUrl: string | undefined;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getWeapon().subscribe({
      next: (data) => {
        console.log('Received data: ', data);
        this.weaponDetails = data;
        this.imageUrl = data.image;
        console.log('Assigned weaponDetails: ', this.weaponDetails);
        console.log('Image URL: ', this.imageUrl);
      },
      error: (err) => {
        console.error('Failed to fetch data:', err);
      },
    });
  }
}
