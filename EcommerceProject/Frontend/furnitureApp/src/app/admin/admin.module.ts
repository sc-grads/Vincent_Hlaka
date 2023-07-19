import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin/admin.component';
import { UsersComponent } from './admin/users/users.component'; // Import the UsersComponent
import { ProductsComponent } from './admin/products/products.component';
import { DashboardComponent } from './admin/dashboard/dashboard.component';

@NgModule({
  declarations: [
    AdminComponent,
    UsersComponent, // Add the UsersComponent to the declarations array
    ProductsComponent,
    DashboardComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
   AdminComponent
   ]
})
export class AdminModule { }
