import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  customer_email: string = '';
  password: string = '';

  constructor(private http: HttpClient, private router: Router) { }

  onSubmit() {
    const data = {
      'customer_email': this.customer_email,
      'password': this.password,
    };

    this.http.post<any>('http://localhost:5000/login', data).subscribe(
      response => {
        console.log(response);
        // handle success response here
        if (response.message === 'Login successful') {
          this.router.navigate(['/catalogue']); // navigate to catalogue page
        } else {
          // handle invalid login
          // show an error message or perform any other necessary action
        }
      },
      error => {
        console.error(error);
        // handle error response here
        // show an error message or perform any other necessary action
      }
    );
  }
}





