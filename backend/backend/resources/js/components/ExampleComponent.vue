<template>

    <div class="uk-section uk-section-muted uk-preserve-color">
        <div class="uk-container">

            <div class="uk-grid-match uk-child-width-expand@m" uk-grid>

                <div>
                    <div class="uk-card uk-card-primary uk-card-body">
                        <h3 class="uk-card-title">Default</h3>
                        <ul class="uk-list">
                            <li><a class="uk-link-muted" href="#">Profiel</a></li>
                            <li><a class="uk-link-muted" href="#">Activiteit</a></li>
                            <li><a class="uk-link-muted" href="#">Uitloggen</a></li>
                        </ul>
                    </div>
                </div>

                <div>
                    <div class="uk-card uk-card-default uk-card-body">
                        <line-chart :chart-data="datacollection"></line-chart>
                    </div>
                </div>
                
            </div>

        </div>
    </div>

</template>

<script>
  import LineChart from './LineChart.vue'

  export default {
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: [this.getRandomInt(), this.getRandomInt()],
          datasets: [
            {
              label: 'Activiteiten',
              backgroundColor: '#f87979',
              data: [this.getRandomInt(), this.getRandomInt()]
            }
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }
    }
  }

//   <div class="uk-child-width-1-2 uk-text-center" uk-grid>

//         <div>
//             <div class="uk-card uk-card-default uk-card-body">
//                 <div class="small">
//                     <line-chart :chart-data="datacollection"></line-chart>
//                 </div>
//             </div>
//         </div>

//         <div>
//             <div class="uk-child-width-1-2" uk-grid>
//                 <div>
//                   Hi
//                 </div>
//                 <div>
//                     Hi
//                 </div>
//             </div>
//         </div>
//     </div>
</script>