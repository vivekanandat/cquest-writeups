<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $role = $_POST["role"];

    $valid_users = [
        "user" => "admin",
        "admin" => "admin"
    ];

    if (isset($valid_users[$role]) && $valid_users[$role] == $password) {
        if ($role == "admin") {
            echo "Login successful! Here is your flag: FLAG{Th1s_is_Bas1c_Int3rc3ption}";
        } else {
            echo "Login successful! But no flag for users.";
        }
    } else {
        echo "Invalid credentials.";
    }
}
?>
