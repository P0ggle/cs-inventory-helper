import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { ShowWeaponDetailsComponent } from "./components/show-weapon-details/show-weapon-details.component"; // Adjust the path as necessary

const routes: Routes = [
  {
    path: "weapons",
    component: ShowWeaponDetailsComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
