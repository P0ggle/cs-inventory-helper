import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowWeaponDetailsComponent } from './show-weapon-details.component';

describe('ShowWeaponDetailsComponent', () => {
  let component: ShowWeaponDetailsComponent;
  let fixture: ComponentFixture<ShowWeaponDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ShowWeaponDetailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ShowWeaponDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
