<template>
    <div class="not-found vh-100 d-flex justify-content-center align-items-center">
        <div class="404-text text-center">
            <img src="@/assets/404-not-found.png" alt="" class="img-fluid w-25">
            <h1 class="lh-1">404 - Page Not Found</h1>
            <p class="text-secondary">The page you are looking for does not exist.</p>
            <router-link to="/" class="btn btn-primary">Go to Homepage</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "NotFound",
    };
</script>