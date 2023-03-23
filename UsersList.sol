// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;
contract UsersList {
    // uint phoneNumber;
    uint256 phoneNumber;
    struct User {
        string first_name;
		string last_name;
		string username;
		string password;
		string email;
		string role;
        string phoneNumber;
    
    }
    User[] public users;
    mapping(string => string) public emailToPhoneNumber;
     
    function retrieve() public view returns (User[] memory){
        return users; 
    }
    
    function addUser(string memory _first_name, string memory _last_name, string memory _username, string memory _password, string memory _email, string memory _phoneNumber, string memory _role) public {
        users.push(User(_first_name,_last_name, _username, _password, _email, _role, _phoneNumber)); 
        emailToPhoneNumber[_email] = _phoneNumber;
    }
    
}