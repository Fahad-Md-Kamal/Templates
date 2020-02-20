import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { DefaultComponent } from './default.component';
import { HomeComponent } from 'src/app/modules/home/home.component';
import { SharedModule } from 'src/app/shared/shared.module';
import { MaterialModule } from 'src/app/utils/material/material.module';


@NgModule({
  declarations: [
    DefaultComponent,
    HomeComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    SharedModule,
    MaterialModule
  ]
})
export class DefaultModule { }
