import logging


class VM(object):
    def __init__(self, vcenter, vm_name):
        self._vcenter = vcenter
        self._vm_name = vm_name
        self._vm = self.find()

    def power_on(self):
        if not self.exists():
            return

        if not self.is_powered_off():
            return

        logging.info("power_on %s ", self._vm_name)
        url = f"/rest/vcenter/vm/{self.get_id()}/power/start"
        self._vcenter.post(url)

    def power_off(self):
        if not self.exists():
            return

        if self.is_powered_off():
            return

        logging.info("power_off %s ", self._vm_name)
        url = f"/rest/vcenter/vm/{self.get_id()}/power/stop"
        self._vcenter.post(url)

    def find(self):
        url = "/rest/vcenter/vm"
        response = self._vcenter.get(url, params={"filter.names.1": self._vm_name})
        logging.debug(response.text)
        if len(response.json()['value']) == 0:
            return None
        return response.json()['value'][0]

    def exists(self):
        self._vm = self.find()
        if self._vm is None:
            logging.info("%s not exists", self._vm_name)
            return False
        logging.info("%s exists", self._vm_name)
        return True

    def is_powered_off(self):
        if self._vm['power_state'] == 'POWERED_OFF':
            logging.info("%s is_powered_off ", self._vm_name)
            return True
        logging.info("%s is powered on ", self._vm_name)
        return False

    def get_id(self):
        logging.info("get_id %s", self._vm_name)
        return self._vm['vm']
