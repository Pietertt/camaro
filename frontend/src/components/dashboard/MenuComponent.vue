<template>
    <div class="uk-container">
        <nav class="uk-navbar-container uk-navbar-transparent" uk-navbar>
            <div class="uk-navbar-left">
                <ul class="uk-navbar-nav">
                    <li><router-link to="/dashboard" exact-active-class="uk-active">Dashboard</router-link></li>
                    <li><router-link to="/activities">Activiteiten</router-link></li>
                    <li><router-link to="/logout">Uitloggen</router-link></li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    
    @Component
    export default class MenuComponent extends Vue {
       
    }
    
</script>