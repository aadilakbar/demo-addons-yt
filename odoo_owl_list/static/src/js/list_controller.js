/** @odoo-module */

import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';

export class OdooOWLListController extends ListController {
   setup() {
       super.setup();
   }

   showCustomers() {
       this.actionService.doAction({
          type: 'ir.actions.act_window',
          res_model: 'res.partner',
          name:'Customers',
          view_mode: 'tree,form',
          view_type: 'form',
          views: [[false, 'tree'], [false, 'form']],
          target: 'current',
          res_id: false,
      });
   }
}


const viewRegistry = registry.category("views");
export const OWLListController = {
    ...listView,
    Controller: OdooOWLListController,
};
viewRegistry.add("owl_list_controller", OWLListController);