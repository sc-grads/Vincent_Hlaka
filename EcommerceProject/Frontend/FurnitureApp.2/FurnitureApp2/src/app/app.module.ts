import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { AboutComponent } from './components/about/about.component';
import { CheckoutComponent } from './components/checkout/checkout.component';
import { CatalogueComponent } from './components/catalogue/catalogue.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component';
import { AdminUsersComponent } from './components/admin-users/admin-users.component';
import { AdminProductsComponent } from './components/admin-products/admin-products.component';
import { AdminComponent } from './components/admin/admin.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'catalogue', component: CatalogueComponent },
  { path: 'about', component: AboutComponent },
  { path: 'checkout', component: CheckoutComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'admin-users', component: AdminUsersComponent },
  { path: 'admin-products', component: AdminProductsComponent },
  { path: '**', component: HomeComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    CheckoutComponent,
    CatalogueComponent,
    LoginComponent,
    SignupComponent,
    AdminDashboardComponent,
    AdminProductsComponent,
    AdminUsersComponent,
    AdminComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
