import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FullwidthComponent } from './fullwidth.component';
import { MaterialModule } from 'src/app/utils/material/material.module';
import { SharedModule } from 'src/app/shared/shared.module';
import { RouterModule } from '@angular/router';
import { AuthComponent } from 'src/app/modules/auth/auth.component';

@NgModule({
  declarations: [
    FullwidthComponent,
    AuthComponent
  ],
  imports: [
    CommonModule,
    MaterialModule,
    SharedModule,
    RouterModule
  ],
})
export class FullwidthModule { }
