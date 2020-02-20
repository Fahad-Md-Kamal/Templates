import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';



@NgModule({
  declarations: [
    HomeComponent, 
    AuthComponent
  ],
  imports: [
    CommonModule
  ]
})
export class ModulesModule { }
