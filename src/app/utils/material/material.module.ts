import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MatToolbarModule } from "@angular/material/toolbar";
import {
  MatIconModule,
  MatButtonModule,
  MatMenuModule,
  MatCardModule,
  MatDividerModule,
  MatListModule,
  MatExpansionModule,
  MatFormFieldModule,
  MatInputModule
} from "@angular/material";
import { MatSidenavModule } from '@angular/material';


import { FlexLayoutModule } from '@angular/flex-layout';

@NgModule({
  declarations: [
  ],
  exports: [
    CommonModule,
    MatSidenavModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    MatDividerModule,
    MatListModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatInputModule,
    FlexLayoutModule
  ]
})
export class MaterialModule { }