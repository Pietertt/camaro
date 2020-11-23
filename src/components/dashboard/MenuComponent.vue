<template>
    <div class="uk-card uk-card-default">
        <div class="uk-card-body">
        <h3 class="uk-card-title">Menu</h3>
            <ul class="uk-list">
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li>Profiel</li>
                <li><router-link to="/dashboard/activiteiten">Activiteiten</router-link></li>
                <li><router-link to="/">Uitloggen</router-link></li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts">

    export default {
       
    }
    
</script>